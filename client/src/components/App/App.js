import React, { Component } from 'react';
import './App.css';
import LawnList from '../LawnList/LawnList';

class App extends Component {
  render() {
    return (
      <div>
        <header>
          <p>Welcome to The Lawn Journal</p>
        </header>

        <LawnList />
      </div>
    );
  }
}

export default App;
