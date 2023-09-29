document.getElementById("reportForm").addEventListener("submit", function(event) {
            event.preventDefault();

            const country = document.getElementById("country").value;
            const league = document.getElementById("league").value;
            const team = document.getElementById("team").value;

            // Construa a URL para o endpoint /report com os parâmetros da consulta
            const url = `/report?country=${encodeURIComponent(country)}&league=${encodeURIComponent(league)}&team=${encodeURIComponent(team)}`;

            // Redirecione o usuário para a URL construída
            window.location.href = url;
        });