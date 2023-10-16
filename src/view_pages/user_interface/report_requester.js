// Dados fictícios de ligas e times por país
const leaguesByCountry = {
    brazil: ["Brasileirão", "Brasileirão Serie B"],
    spain: ["La Liga", "Segunda División"]
    // Adicione mais países e ligas aqui
};

const teamsByLeague = {
    brasileirao: ["Flamengo", "São Paulo", "Palmeiras"],
    brasileiraoserieb: ["Vasco da Gama", "Cruzeiro", "Coritiba"],
    laliga: ["Real Madrid", "Barcelona", "Atletico Madrid"],
    segundadivision: ["Real Zaragoza", "Espanyol", "Mallorca"]
    // Adicione mais ligas e times aqui
};

function populateLeagues() {
    const selectedCountry = countrySelect.value;
    const leagues = leaguesByCountry[selectedCountry];
    leagueSelect.innerHTML = "";
    teamSelect.innerHTML = "<option value='' disabled selected>Selecione um time</option>";
    leagues.forEach(league => {
        const option = document.createElement("option");
        option.value = league.toLowerCase().replace(/\s/g, "");
        option.textContent = league;
        leagueSelect.appendChild(option);
    });
}

function populateTeams() {
    const selectedLeague = leagueSelect.value;
    const teams = teamsByLeague[selectedLeague];
    teamSelect.innerHTML = "<option value='' disabled selected>Selecione um time</option>";
    teams.forEach(team => {
        const option = document.createElement("option");
        option.value = team.toLowerCase().replace(/\s/g, "");
        option.textContent = team;
        teamSelect.appendChild(option);
    });
}

const countrySelect = document.getElementById('country');
const leagueSelect = document.getElementById('league');
const teamSelect = document.getElementById('team');
const generateReportButton = document.getElementById('generate-report');

countrySelect.addEventListener('change', populateLeagues);
leagueSelect.addEventListener('change', populateTeams);

generateReportButton.addEventListener('click', function() {
    const selectedCountry = countrySelect.value;
    const selectedLeague = leagueSelect.value;
    const selectedTeam = teamSelect.value;

    const reportText = `País: ${selectedCountry}, Liga: ${selectedLeague}, Time: ${selectedTeam}`;

    const url = `/report?country=${encodeURIComponent(selectedCountry)}&league=${encodeURIComponent(selectedLeague)}&team=${encodeURIComponent(selectedTeam)}`;
    window.location.href = url;
});


populateLeagues();
