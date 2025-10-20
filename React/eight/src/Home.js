import React, { useState } from 'react';

function Home() {

    const [items, setItems] = useState([
        { name: 'Apple', completed: false },
        { name: 'Banana', completed: false },
        { name: 'Tea', completed: false },
        { name: 'Coffee', completed: false }
    ]);

    const toggleItem = (index) => {
        const newItems = [...items];
        newItems[index].completed = !newItems[index].completed;
        setItems(newItems);
    };

    const totalCompleted = items.filter(item => item.completed).length;

    return (
        <div style={{ textAlign: 'left', padding: '20px' }}>
            <h2>Home Page:</h2>
            <h2>Shopping List:</h2>
            {items.map((item, index) => (
                <div key={index} style={{ display: 'flex', justifyContent: 'flex-start'}}>
                    <input
                        type="checkbox"
                        checked={item.completed}
                        onChange={() => toggleItem(index)}
                        style={{ marginRight: '10px' }}
                    />
                    <label>
                        {item.name} {item.completed ? '+' : '-'}
                    </label>
                </div>
            ))}
            <hr />
            <div style={{ display: 'flex' }}>
                <span>Total Completed:</span>
                <span>{totalCompleted}</span>
            </div>
        </div>
    );
}

export default Home;