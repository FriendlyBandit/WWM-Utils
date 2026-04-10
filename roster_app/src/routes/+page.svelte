<script>
    let roster = {
        "team 1": ["Xeon", "astro ★", "𝕸ï𝖘𝖔", "Starlit-Qin", "Shokyute (realest)"],
        "team 2": ["Jaeh", "Shatian", "Ares Targaryen", "XxLivius1xX", "雲白 (Cloud)"],
        "team 3": ["ThresherOfSouls", "stayquiet", "STAR", "厄Jinx运", "Zinnia"],
        "team 4": ["FriendlyBandit", "Sangka", "Yuèfengshé", "Lilith (Hades)", "Silly (Shu-Ngaa)"],
        "team 5": ["Moika", "Noills", "Leesh", "Choloepus", "Duduxai"],
        "team 6": ["J Cobain", "Peachtea", "monger", "Shurisan", "scarlet"]
    };

    let roles = {
        "team 1": ["Mo + Dual Blade", "Mo + Tank Spear", "Nameless", "Healer", "Healer"],
        "team 2": ["Mo + Dual Blade", "Mo + Tank Spear", "Nameless", "Nameless", "Healer"],
        "team 3": ["Mo + Fan", "Nameless", "Nameless", "Nameless", "Healer"],
        "team 4": ["Mo + Fan", "Nameless", "Nameless", "Healer", "Healer"],
        "team 5": ["Mo + Dual Blade", "Mo + Tank Spear", "Nameless", "Dust", "Healer"],
        "team 6": ["Mo + Tang Dao", "99", "Nameless", "Nameless", "Healer"]
    };

    let rotation = {
        "team 1": ["Suck 1, Antiheal 1", "Suck 2", "Shield 1", "Heal 1", "Heal 2"],
        "team 2": ["Suck 3, Antiheal 2", "Suck 4", "Shield 2", "Shield 3", "Heal 3"],
        "team 3": ["Suck 5", "Shield 4", "Shield 5", "Shield 6", "Heal 4"],
        "team 4": ["", "", "", "", ""],
        "team 5": ["", "", "", "", ""],
        "team 6": ["", "", "", "", ""]
    };

    const tank = "#ffbf69";
    const dps = "#f25c54";
    const healer = "#92e6a7";

    const colorMap = new Map();
    colorMap.set("Mo + Dual Blade", tank)
    colorMap.set("Mo + Tank Spear", tank)
    colorMap.set("Mo + Tang Dao", tank)
    colorMap.set("Mo + Fan", tank)
    colorMap.set("Healer", healer)
    colorMap.set("Nameless", dps)
    colorMap.set("Dust", dps)
    colorMap.set("Fanbrella", dps)
    colorMap.set("99", dps)

    const leftTeams = ["team 1", "team 2", "team 3"];
    const rightTeams = ["team 4", "team 5", "team 6"];

    const rsvpRoles = ["tank", "damage", "healer", "tentative", "declined"];
    const rsvpStatus = {};
    $: rowCount = 0;
    let tableBuckets = {
        tank: [],
        damage: [],
        healer: [],
        tentative: [],
        declined: []
    };

    const globalRoles = {};

    function apolloPaste(event) {
        const apollo_data = event.target.value;
        const lines = apollo_data.split("\n");
        const buckets = {};
        let currentRole = null;

        for (let line of lines) {
            line = line.trim();
            if (!line) continue;

            if (line.startsWith(":")) {
                currentRole = line.split(":")[1].trim();
                if (!buckets[currentRole]) {
                    buckets[currentRole] = [];
                }
            } else if (currentRole) {
                buckets[currentRole].push(line);
            }
        }

        const maxLen = Math.max(...Object.values(buckets).map(arr => arr.length));

        for (const role in buckets) {
            for (const mem_idx in buckets[role]){
                let member = buckets[role][mem_idx];
                
                globalRoles[member] = role;
                
                if (role == "tentative"){
                    rsvpStatus[member] = "#c599f2"
                }else if (role == "declined"){
                    rsvpStatus[member] = "#d48383"
                }else{
                    rsvpStatus[member] = "#99b4f2"
                }
            }
            while (buckets[role].length < maxLen) {
                buckets[role].push("");
            }
        }
        
        tableBuckets = buckets;
        rowCount = maxLen;
    }

    let table1, table2;
    async function copyTable(tableElement) {
        const html = tableElement.outerHTML;
        const text = tableElement.innerText;

        const htmlBlob = new Blob([html], { type: "text/html" });
        const textBlob = new Blob([text], { type: "text/plain" });

        const data = [
            new ClipboardItem({
                "text/html": htmlBlob,
                "text/plain": textBlob
            })
        ];

        await navigator.clipboard.write(data);
    }

    function handleDragStart(e, text, color, role) {
        const data = JSON.stringify({ text, color });
        
        e.dataTransfer.setData("application/json", data);
        e.dataTransfer.dropEffect = "copy";
    }

    function handleDrop(e, team, memberIdx) {
        e.preventDefault();
        const rawData = e.dataTransfer.getData("application/json");
        if (!rawData) return;
        
        const prev_member = roster[team][memberIdx]

        const { text, color } = JSON.parse(rawData);
        roster[team][memberIdx] = text;
        
        let role = null;
        if(prev_member in globalRoles){
            role = globalRoles[prev_member];
        }

        let tempTableBuckets = {}
        
        for (const role in tableBuckets){
            tempTableBuckets[role] = tableBuckets[role].filter(item => item !== "");
            tempTableBuckets[role] = tempTableBuckets[role].filter(item => item !== text);
        }
        
        if (prev_member in globalRoles){
            tempTableBuckets[role].push(prev_member)
        }
        
        const maxLen = Math.max(...Object.values(tempTableBuckets).map(arr => arr.length));
        rowCount = maxLen;
        for (const role in tempTableBuckets) {
            while (tempTableBuckets[role].length < maxLen) {
                tempTableBuckets[role].push("");
            }
        }
        tableBuckets = tempTableBuckets
    }

    function removeRostered(){
        const rosteredMembers = new Set()
        rosteredMembers.add("")
        for (const team in roster){
            for (const member in roster[team]){
                rosteredMembers.add(roster[team][member])
            }
        }
        
        for (const team in tableBuckets) {
            tableBuckets[team] = tableBuckets[team].filter(member => !rosteredMembers.has(member));
        }

        const maxLen = Math.max(...Object.values(tableBuckets).map(arr => arr.length));
        rowCount = maxLen;
        for (const role in tableBuckets) {
            while (tableBuckets[role].length < maxLen) {
                tableBuckets[role].push("");
            }
        }                
    }

    function moveMemberToFill(member, team){
        let memberRole = null;
        if(member in globalRoles){
            memberRole = globalRoles[member];
        }
        
        let rosterIdx = roster[team].indexOf(member);
        roster[team][rosterIdx] = "PLACEHOLDER";

        let tempTableBuckets = {};
        for (const role in tableBuckets){
            tempTableBuckets[role] = tableBuckets[role].filter(item => item !== "");
        }
        
        if (member in globalRoles){
            if(!(member in tempTableBuckets[memberRole])){
                tempTableBuckets[memberRole].push(member);
                console.log("not here?");
                
            } 
        }

        const maxLen = Math.max(...Object.values(tempTableBuckets).map(arr => arr.length));
        rowCount = maxLen;        
        for (const role in tempTableBuckets) {
            while (tempTableBuckets[role].length < maxLen) {
                tempTableBuckets[role].push("");
            }
        }
        tableBuckets = tempTableBuckets;
    }
</script>

<div class="in_wrap">
    <div style="margin-left: auto; margin-right: auto;">Apollo Paste</div>
    <textarea name="apollo" id="apollo" on:input={apolloPaste}></textarea>
    <div id="table_container">
        <table bind:this={table1}>
            <thead>
                <tr>
                    <th>Build</th><th>Rotation</th><th>Member</th>
                    <th>Build</th><th>Rotation</th><th>Member</th>
                </tr>
            </thead>
            <tbody>
                {#each [0,1,2] as i}
                    <tr style="background-color: #f0f0f0;">
                        <td style="text-align: center;" colspan="3"><strong>{leftTeams[i].toUpperCase()}</strong></td>
                        <td style="text-align: center;" colspan="3"><strong>{rightTeams[i].toUpperCase()}</strong></td>
                    </tr>

                    {#each [0, 1, 2, 3, 4] as memberIdx}
                        <tr>
                            <td style="background-color: {colorMap.get(roles[leftTeams[i]][memberIdx])}">{roles[leftTeams[i]][memberIdx]}</td>
                            <td>{rotation[leftTeams[i]][memberIdx]}</td>
                            <td 
                                on:dragover|preventDefault
                                on:drop={(e) => handleDrop(e, leftTeams[i], memberIdx)}
                                on:dblclick={() => moveMemberToFill(roster[leftTeams[i]][memberIdx], leftTeams[i])}
                                style="background-color: {rsvpStatus[roster[leftTeams[i]][memberIdx]]};"
                            >
                                {roster[leftTeams[i]][memberIdx]}
                            </td>

                            <td style="background-color: {colorMap.get(roles[rightTeams[i]][memberIdx])}">{roles[rightTeams[i]][memberIdx]}</td>
                            <td>{rotation[rightTeams[i]][memberIdx]}</td>
                            <td 
                                on:dragover|preventDefault
                                on:drop={(e) => handleDrop(e, rightTeams[i], memberIdx)}
                                on:dblclick={() => moveMemberToFill(roster[rightTeams[i]][memberIdx], rightTeams[i])}
                                style="background-color: {rsvpStatus[roster[rightTeams[i]][memberIdx]]};"
                            >
                                {roster[rightTeams[i]][memberIdx]}
                            </td>                        
                        </tr>
                    {/each}
                {/each}
            </tbody>
        </table>
        <button on:click={() => copyTable(table1)} style="padding: 10px; cursor: pointer;">
            Copy Table
        </button>
    </div>
</div>
<div id="rsvpContainer">
    <div id="rsvp" class:rsvp_filled={rowCount > 0}>
        {#if rowCount > 0}
            <table bind:this={table2}>
                <thead>
                    <tr>
                        <th>Tank</th>
                        <th>Damage</th>
                        <th>Healer</th>
                        <th>Tentative</th>
                        <th>Declined</th>
                    </tr>
                </thead>
                <tbody>
                    {#each Array(rowCount) as _,i}
                        <tr>
                            {#each rsvpRoles as role}
                                <td 
                                    draggable="true"
                                    on:dragstart={(e) => handleDragStart(e, tableBuckets[role][i], rsvpStatus[tableBuckets[role][i]], role)}
                                    style="background-color: {rsvpStatus[tableBuckets[role][i]]}; cursor: grab;"
                                >
                                    {tableBuckets[role][i]}
                                </td>
                            {/each}
                        </tr>
                    {/each}
                </tbody>
            </table>
            <div id="button-wrapper">
                <button on:click={() => copyTable(table2)} style="padding: 10px; cursor: pointer;">
                    Copy Table
                </button>
                <button on:click={removeRostered} style="padding: 10px; cursor: pointer;">
                    Remove Rostered
                </button>
            </div>
            
        {:else}
            <p>RSVP Will Generate Here On Paste</p>
        {/if}
    </div>
</div>

<style>
    #button-wrapper{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    #button-wrapper>button{
        margin-top: 0px;
        margin-bottom: 10px;
    }

    .in_wrap {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1ch;
    }

    #rsvpContainer{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        margin-top: 1ch;
    }

    #rsvp{
        display: flex;
    }

    .rsvp_filled{
        margin-left: 25ch;
    }

    #apollo{
        width: 30ch;
        height: 30ch;
        margin-left: auto;
        margin-right: auto;
    }

    table {
        border-collapse: collapse;
        border: 2px solid rgb(140 140 140);
        font-family: sans-serif;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }

    #table_container{
        display: flex;
        margin-left: 25ch;
    }

    button{
        height: 10ch;
        width: 15ch;
        text-align: center;
        margin: auto;
    }

    thead,
    th,
    td {
    border: 1px solid rgb(160 160 160);
    padding: 8px 10px;
    }

    td:last-of-type {
    text-align: center;
    }

    tbody > tr:nth-of-type(even) {
    background-color: rgb(237 238 242);
    }

</style>