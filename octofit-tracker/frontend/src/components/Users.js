import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users component: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Users component: fetched data', data);
        const usersData = Array.isArray(data) ? data : data.results || [];
        setUsers(usersData);
      })
      .catch((err) => {
        console.error('Users component: error fetching data', err);
        setError(err.message);
      });
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <a href="/" className="btn btn-secondary mb-3">&larr; Back to Homepage</a>
      <h2>Users</h2>
      {error && <div className="alert alert-danger">Error: {error}</div>}
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Username</th>
            <th>Email</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => {
            const capitalize = (str) => str ? str.charAt(0).toUpperCase() + str.slice(1) : '';
            const fullName = `${capitalize(user.first_name)} ${capitalize(user.last_name)}`.trim();
            return (
              <tr key={user._id || user.id}>
                <td>{user.first_name}</td>
                <td>{user.last_name}</td>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{fullName}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
