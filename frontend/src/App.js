import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Footer from './components/Footer';
import Header from './components/header';
import HomeMain from './components/HomeMain';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import Preferences from './components/Preferences';
import HighlightsPage from './components/HighlightsPage';
import ArticleDetail from './components/ArticleDetail';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Routes>
          {/* Route vers la page d'accueil */}
          <Route path="/" element={<HomeMain />} />

          {/* Route vers la page de connexion */}
          <Route path="/login" element={<Login />} />

          <Route path="/preferences" element={ <ProtectedRoute> <Preferences /> </ProtectedRoute> } />

          <Route path="/highlights" element={<ProtectedRoute> <HighlightsPage /> </ProtectedRoute>} />

          <Route path="/article/:id" element={<ArticleDetail />} /> {/* Route dynamique */}


        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;

