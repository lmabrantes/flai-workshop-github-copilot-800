import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Activities component: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Activities component: fetched data', data);
        const activitiesData = Array.isArray(data) ? data : data.results || [];
        setActivities(activitiesData);
      })
      .catch((err) => {
        console.error('Activities component: error fetching data', err);
        setError(err.message);
      });
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      {error && <div className="alert alert-danger">Error: {error}</div>}
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>User</th>
            <th>Activity Type</th>
            <th>Duration (min)</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity) => (
            <tr key={activity._id || activity.id}>
              <td>{activity.user}</td>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
              <td>{activity.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
