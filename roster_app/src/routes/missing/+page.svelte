<script>
    const gvgRoster = [
        "Arael",
        "Ares Targaryen",
        "astro ★",
        "Av (velrith)",
        "carpybarpa (郑心月)",
        "Cathedrals",
        "Choloepus",
        "CynicalInsight",
        "Dosed",
        "Duduxai",
        "Entropy",
        "FriendlyBandit",
        "HahahaxD",
        "Hakaijin",
        "Haku",
        "Hamsup",
        "Henada",
        "HenTieFukada",
        "Hevn",
        "J Cobain",
        "Jaeh",
        "JessBell",
        "Jun",
        "Kal X",
        "KingBreaker",
        "Kow",
        "Leesh",
        "Lilith (Hades)",
        "MaDpOo",
        "MindlessWanderer",
        "𝕸ï𝖘𝖔",
        "monger",
        "Noills",
        "Panda",
        "PandaStick (Rarest)",
        "Peachtea",
        "Sangka",
        "scarlet",
        "Shatian",
        "Shen-Yuelin",
        "Shizhu",
        "Shokyute (realest)",
        "Shurisan",
        "Silly (Shu-Ngaa)",
        "STAR",
        "stayquiet",
        "Sunora",
        "Tèar",
        "Tharianrix",
        "ThresherOfSouls",
        "whh",
        "Xeon",
        "Xìong",
        "XxLivius1xX",
        "YooSeo-yeon",
        "Yuèfengshé",
        "Zetianna",
        "Zinnia",
        "乐童儿 (TongTong)",
        "厄Jinx运",
        "雲白 (Cloud)",
    ];

    let missingPpl = "";
    let apolloInput = "";

    function apolloPaste(inputPaste) {
        const rsvpMembers = [];
        for (const line of inputPaste.split("\n")) {
            if (!line.includes(":")) {
                rsvpMembers.push(line);
            }
        }
        
        const missingMembers = []
        for (const member of gvgRoster) {
            if (!rsvpMembers.includes(member)) {
                missingMembers.push("@" + member);
            }
        }
        
        const memberStr = missingMembers.join("\n")
        console.log(memberStr);
        
        missingPpl = memberStr;
    }

    function copyMissing(missingList) {
        const copyText = missingList.replaceAll("\n", " ")
        navigator.clipboard.writeText(copyText);
    }
</script>

<div id="container">
    <div>Apollo Paste</div>
    <textarea
        name="apollo"
        id="apollo"
        bind:value={apolloInput}
        on:input={() => apolloPaste(apolloInput)}
    ></textarea>
    <div>Missing:</div>
    <textarea bind:value={missingPpl} name="missing" id="missing"
    ></textarea>
    <button on:click={() => copyMissing(missingPpl)}>Copy Missing</button>
</div>



<style>
    #container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1ch;
    }

    #apollo,
    #missing {
        height: 45ch;
        width: 30ch;
    }
</style>
