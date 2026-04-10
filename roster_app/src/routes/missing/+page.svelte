<script>
    const gvgRoster = ["Moika",
        "Sangka",
        "Zariion",
        "whh",
        "ThresherOfSouls",
        "Shatian",
        "stayquiet",
        "ズﾑﾚ ﾒ",
        "Rongcheng",
        "Xìong",
        "astro ★",
        "Starlit-Qin",
        "Arael",
        "Tèar",
        "Shizhu",
        "Xeon",
        "Ares Targaryen",
        "Liu'Wulang",
        "𝕸ï𝖘𝖔",
        "FriendlyBandit",
        "Shen-Yuelin",
        "Kow",
        "Shuri-san",
        "Apollo",
        "Zinnia",
        "HenTieFukada",
        "Peachtea",
        "Yuèfengshé",
        "almightyscum",
        "scarlet",
        "厄Jinx运",
        "CynicalInsight",
        "cobain",
        "Dosed",
        "YooSeo-yeon",
        "雲白 (Cloud)",
        "KingBreaker",
        "Ferla",
        "NellieMellie",
        "Tharianrix",
        "乐童儿 (TongTong)",
        "Lilith (Hades)",
        "Jun",
        "Węilóng",
        "J Cobain",
        "monger",
        "Entropy",
        "MindlessWanderer",
        "XxLivius1xX",
        "Hakaijin",
        "Jaeh",
        "guangguang",
        "Noills",
        "Shokyute (realest)",
        "Cathedrals",
        "STAR",
        "Henada",
        "Choloepus",
        "Duduxai",
        "Parmesan",
        "Leesh",
        "Silly (Shu-Ngaa)"];

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
