import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts component: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Workouts component: fetched data', data);
        const workoutsData = Array.isArray(data) ? data : data.results || [];
        setWorkouts(workoutsData);
      })
      .catch((err) => {
        console.error('Workouts component: error fetching data', err);
        setError(err.message);
      });
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <a href="/" className="btn btn-secondary mb-3">&larr; Back to Homepage</a>
      <h2>Workouts</h2>
      {error && <div className="alert alert-danger">Error: {error}</div>}
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout) => (
            <tr key={workout._id || workout.id}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;
