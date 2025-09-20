import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  state = {
    todos: [],
    error: null,
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then((res) => {
        console.log("Response:", res); // برای تست توی کنسول
        this.setState({ todos: res.data, error: null });
      })
      .catch((err) => {
        console.error("Error:", err); // برای تست توی کنسول
        this.setState({ error: err.message });
      });
  }

  render() {
    return (
      <div>
        <h2>Todos</h2>

        {this.state.error && (
          <div style={{ color: "red" }}>
            خطا: {this.state.error}
          </div>
        )}

        {this.state.todos.length > 0 ? (
          this.state.todos.map((item) => (
            <div key={item.id}>
              <h3>{item.title}</h3>
              <p>{item.body}</p>
            </div>
          ))
        ) : (
          !this.state.error && <p>هیچ داده‌ای وجود ندارد.</p>
        )}
      </div>
    );
  }
}

export default App;
