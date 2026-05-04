import './App.css'

function App() {
  const iframeSrc = `/wedding-invitation.html${window.location.search}`

  return (
    <iframe
      className="invitation-frame"
      src={iframeSrc}
      title="Wedding Invitation"
    />
  )
}

export default App
