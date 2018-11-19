import React, { Component } from 'react';
import './LawnList.css';

class LawnList extends Component {

  constructor() {
      super();
      this.state = {
          lawns: []
      }
  }

  componentDidMount() {
    fetch('http://localhost:5000/api/lawns')
    .then(results => {
        return results.json()
    }).then(data => {
        let lawns = data.lawns.map((lawn) => {
            return (
                <li key={Math.floor(Math.random() * 100)}>{lawn.name}</li>
            )
        })
        this.setState({lawns: lawns});
    })
  }

  render() {
    return (
      <div>
        <h2>Lawn List</h2>
        <ul>{this.state.lawns}</ul>
      </div>
    );
  }
}

export default LawnList;