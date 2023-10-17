const leaguesByCountry = {
    brazil_teams: ["serie_a", "brasileiraoserieb"],
    england_teams: ["premier_league", "efl_championship"]
};

const teamsByLeague = {
    serie_a: ["Sport Club Corinthians Paulista", "São Paulo Futebol Clube", "Grêmio Foot-Ball Porto Alegrense"],
    brasileiraoserieb: ["Vasco da Gama", "Cruzeiro", "Coritiba"],
    premier_league: ["Manchester City Football Club", "Manchester United Football Club", "Liverpool Football Club"],
    efl_championship: ["Real Zaragoza", "Espanyol", "Mallorca"]
};

function populateLeagues() {
    const selectedCountry = countrySelect.value;
    const leagues = leaguesByCountry[selectedCountry];
    leagueSelect.innerHTML = "";
    teamSelect.innerHTML = "<option value='' disabled selected>Selecione um time</option>";
    leagues.forEach(league => {
        const option = document.createElement("option");
        option.value = league;
        option.textContent = league;
        leagueSelect.appendChild(option);
    });
    populateTeams();
}

function populateTeams() {
    const selectedLeague = leagueSelect.value;
    const teams = teamsByLeague[selectedLeague];
    teamSelect.innerHTML = "<option value='' disabled selected>Selecione um time</option>";
    teams.forEach(team => {
        const option = document.createElement("option");
        option.value = team;
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

generateReportButton.addEventListener('click', function () {
    const selectedCountry = countrySelect.value;
    const selectedLeague = leagueSelect.value;
    const selectedTeam = teamSelect.value;

    const reportText = `País:  ${selectedCountry}, Liga: ${selectedLeague}, Time: ${selectedTeam}`;

    const url = `/report?country=${encodeURIComponent(selectedCountry)}&league=${encodeURIComponent(selectedLeague)}&team=${encodeURIComponent(selectedTeam)}`;
    window.location.href = url;
});

populateLeagues();
populateTeams();
