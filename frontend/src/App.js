import "./App.css";
import React, { useEffect } from "react";
import axios from "axios";

function App() {
  const [users, setUsers] = React.useState([])

  useEffect(() => {
    axios.get("/api").then(res => console.log(res.data))
  }, [])

  // console.log({users})

  return (
    <div className="App">
      Hello World
    </div>
  );
}

export default App;
