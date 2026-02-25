import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams component: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Teams component: fetched data', data);
        const teamsData = Array.isArray(data) ? data : data.results || [];
        setTeams(teamsData);
      })
      .catch((err) => {
        console.error('Teams component: error fetching data', err);
        setError(err.message);
      });
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <a href="/" className="btn btn-secondary mb-3">&larr; Back to Homepage</a>
      <h2>Teams</h2>
      {error && <div className="alert alert-danger">Error: {error}</div>}
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>Team Name</th>
            <th>Members</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team) => (
            <tr key={team._id || team.id}>
              <td>{team.name}</td>
              <td>
                {Array.isArray(team.members)
                  ? team.members.join(', ')
                  : team.members}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;
