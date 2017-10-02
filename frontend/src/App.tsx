import * as React from 'react';
import './App.css';
import axios from 'axios';

const logo = require('./logo.svg');

const API_URL = `http://localhost:81/django/`;

class App extends React.Component {

  state = {
    loading: true,
    token: null,
    todos: [],
  };

  constructor(props: any) {
    super(props);
    this.loadData();
  }

  async loadData() {
    const { data: { token }} = await axios.post(`${API_URL}api-token-auth/`, {
      username: `admin`,
      password: `admin`,
    });
    const todos = (await axios.get(`${API_URL}todos/`, {
      headers: {
        Authorization: `JWT ${token}`,
      }
    })).data;
    this.setState({
      todos,
      loading: false,
      token,
    });
  }

  render() {
    const { loading, todos } = this.state;
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.tsx</code> and save to reload.
        </p>
        <ul className="todos">
          {loading ?
            <li>Loading...</li>
          :
            todos.map((t: any, i) =>
              <li key={i}>{t.description}</li>
            )
          }
        </ul>
      </div>
    );
  }
}

export default App;
