document.getElementById("reportForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const country = document.getElementById("country").value;
            const league = document.getElementById("league").value;
            const team = document.getElementById("team").value;

            const url = `/report?country=${encodeURIComponent(country)}&league=${encodeURIComponent(league)}&team=${encodeURIComponent(team)}`;

            window.location.href = url;
        });