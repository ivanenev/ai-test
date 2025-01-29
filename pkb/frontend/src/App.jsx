import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import DocumentList from './components/DocumentList';
import DocumentViewer from './components/DocumentViewer';

const App = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate loading
    setTimeout(() => setLoading(false), 1000);
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-2xl font-bold text-blue-600">Loading...</div>
      </div>
    );
  }

  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <Link to="/" className="text-xl font-bold text-blue-600">
                    Knowledge Base
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main className="container mx-auto p-8">
          <h1 className="text-3xl font-bold mb-4">Welcome to Knowledge Base</h1>
          <div className="bg-white p-6 rounded-lg shadow">
            <p className="text-gray-700">This is a test content to verify the page is rendering correctly.</p>
            <div className="mt-4">
              <Link 
                to="/test" 
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
              >
                Test Link
              </Link>
            </div>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
