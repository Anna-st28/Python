import React from 'react';
import './App.css';
import Hello from './Hello';
import Length from './Length';
import Form from './Form';
import Range from './Range';

class App extends React.Component {
  render() {
    return (
      <div>
        <Hello />
        <Length />
        <Form />
        <Range />
      </div >
    );
  }
}

export default App;
