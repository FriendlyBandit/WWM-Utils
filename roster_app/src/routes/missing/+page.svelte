<script>
    const gvgRoster = ["Cathedrals",
        "Haku",
        "Peachtea",
        "Apollo",
        "Xeon",
        "EdenXXI",
        "monger",
        "Zetianna",
        "YooSeo-yeon",
        "Jaeh",
        "Entropy",
        "scarlet",
        "雲白 (Cloud)",
        "Yuèfengshé",
        "Dosed",
        "Leesh",
        "Xìong",
        "Arael",
        "Choloepus",
        "HenTieFukada",
        "Zariion",
        "Kow",
        "Zinnia",
        "Ares Targaryen",
        "Shizhu",
        "Tèar",
        "厄Jinx运",
        "Tharianrix",
        "乐童儿 (TongTong)",
        "Starlit-Qin",
        "MindlessWanderer",
        "stayquiet",
        "almightyscum",
        "guangguang",
        "J Cobain",
        "Panda",
        "Silly (Shu-Ngaa)",
        "STAR",
        "Shatian",
        "astro ★",
        "Jun",
        "Duduxai",
        "Henada",
        "CynicalInsight",
        "KingBreaker",
        "Rongcheng",
        "XxLivius1xX",
        "ズﾑﾚ ﾒ",
        "Shurisan",
        "JessBell",
        "Noills",
        "ThresherOfSouls",
        "Lilith (Hades)",
        "𝕸ï𝖘𝖔",
        "Ferla",
        "FriendlyBandit",
        "Sangka",
        "Shokyute (realest)",
        "Shen-Yuelin",
        "whh"
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
