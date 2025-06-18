import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://studious-space-enigma-jw6pwpjv7jcpwq5-8000.app.github.dev/api/teams')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div>
      <h1 className="text-center">Teams</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.name}>
              <td>{team.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;
