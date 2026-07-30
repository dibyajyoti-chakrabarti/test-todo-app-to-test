import { useState, useEffect } from 'react'

function App() {
  const [todos, setTodos] = useState([])
  const [title, setTitle] = useState('')

  useEffect(() => {
    fetch('/api/todos/')
      .then((res) => res.json())
      .then(setTodos)
      .catch(console.error)
  }, [])

  const addTodo = async (e) => {
    e.preventDefault()
    if (!title.trim()) return
    const res = await fetch('/api/todos/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title }),
    })
    const todo = await res.json()
    setTodos([todo, ...todos])
    setTitle('')
  }

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>Todos</h1>
      <form onSubmit={addTodo} style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="New todo…"
          style={{ flex: 1, padding: '0.5rem' }}
        />
        <button type="submit" style={{ padding: '0.5rem 1rem' }}>Add</button>
      </form>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {todos.map((t) => (
          <li key={t.id} style={{ padding: '0.5rem 0', borderBottom: '1px solid #eee' }}>
            {t.title}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
