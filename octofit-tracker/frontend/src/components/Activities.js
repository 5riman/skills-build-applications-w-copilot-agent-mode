import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://studious-space-enigma-jw6pwpjv7jcpwq5-8000.app.github.dev/api/activities')
      .then(response => response.json())
      .then(data => setActivities(data));
  }, []);

  return (
    <div>
      <h1 className="text-center">Activities</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Type</th>
            <th>Duration (mins)</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity.activity_id}>
              <td>{activity.type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
