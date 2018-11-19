import React, { Component } from 'react';
import './App.css';
import LawnList from '../LawnList/LawnList';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Welcome to the Lawn Journal</h1>

        <LawnList />
      </div>
    );
  }
}

export default App;
