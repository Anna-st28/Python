import React from "react";

class Range extends React.Component {
  state = { val: 50 };

  range = (event) => {
    this.setState({ val: event.target.value });
  };

  render() {
    const size = `${this.state.val}px`;
    
    return (
      <>
        <hr />
        <label>Выберите размер квадрата:</label>
        <input type="range" min="50" max="240" value={this.state.val} onChange={this.range} 
        />
        <p>{size}</p>
        <div 
          style={{ 
            width: size, 
            height: size, 
            backgroundColor: 'red'
          }} 
        />
      </>
    );
  }
}

export default Range;