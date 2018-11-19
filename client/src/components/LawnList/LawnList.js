import React, { Component } from 'react';
import './LawnList.css';

class LawnList extends Component {
  render() {
    return (
      <div>
        <h2>Lawn List</h2>
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