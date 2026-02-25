import React from 'react';
import { Routes, Route, NavLink, useNavigate } from 'react-router-dom';
import './App.css';
import logo from './octofitapp-small.png';
import Users from './components/Users';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Workouts from './components/Workouts';

function Home() {
  const navigate = useNavigate();
  const cards = [
    { title: 'Users', path: '/users', description: 'View and manage OctoFit members.' },
    { title: 'Activities', path: '/activities', description: 'Log and track your fitness activities.' },
    { title: 'Leaderboard', path: '/leaderboard', description: 'See who is leading the competition.' },
  ];
  return (
    <div className="welcome-section text-center">
      <h1>Welcome to OctoFit Tracker</h1>
      <p className="lead">Track your fitness activities, join teams, and compete on the leaderboard!</p>
      <div className="row justify-content-center mt-4">
        {cards.map((card) => (
          <div key={card.path} className="col-md-3 mb-4">
            <div
              className="card h-100 shadow-sm"
              style={{ cursor: 'pointer' }}
              onClick={() => navigate(card.path)}
            >
              <div className="card-body d-flex flex-column justify-content-center">
                <h5 className="card-title">{card.title}</h5>
                <p className="card-text">{card.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <NavLink className="navbar-brand" to="/">
            <img src={logo} alt="OctoFit" className="app-logo" />
            OctoFit Tracker
          </NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className="nav-link" to="/users">Users</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/activities">Activities</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/teams">Teams</NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/workouts">Workouts</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
      <footer className="footer">
        &copy; {new Date().getFullYear()} OctoFit Tracker &mdash; Stay active, stay healthy!
      </footer>
    </div>
  );
}

export default App;
