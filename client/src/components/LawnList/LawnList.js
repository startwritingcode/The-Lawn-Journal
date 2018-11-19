import React, { Component } from 'react';
import './LawnList.css';

class LawnList extends Component {
  render() {
    return (
      <div>
        <h1>Lawn List</h1>
        <ul>
            <li>Home Lawn</li>
            <li>Parents Lawn</li>
            <li>Vacation Home</li>
        </ul>
      </div>
    );
  }
}

export default LawnList;