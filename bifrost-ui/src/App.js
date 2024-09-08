import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"; // Import Navigate

import Header from "./components/layout/Header";
import Sidenav from "./components/layout/Sidenav";
import Footer from "./components/layout/Footer";

import Dashboard from "./components/home/Dashboard";

import Adaptors from "./components/apps/Adaptors";

import Scans from "./components/apps/Scans";
import ScanDetails from "./components/apps/scan/ScanDetails";

import Vulnerabilities from "./components/apps/Vulnerabilities";

import Secrets from "./components/apps/Secrets";

import Tags from "./components/configurations/Tags";
import Configurations from "./components/configurations/Configurations";
import VulnerabilityClasses from "./components/configurations/VulnerabilityClasses";
import Workflows from "./components/configurations/Workflows";

import Twitter from "./components/social/Twitter";
import VulnerabilityDetails from "./components/apps/vulnerability/VulnerabilityDetails";

function App() {
  return (
    <div className="App bg-gray-50">
      <BrowserRouter>
      <div className="min-h-screen bg-blue-gray-50/50">
        <Sidenav />
        <div className="p-4 xl:ml-80">
          <Header />
          
            <Routes>
              <Route path="/" element={<Navigate to="/dashboard" />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/bifrost" element={<Adaptors />} />
              <Route path="/adaptors" element={<Adaptors />} />
              <Route path="/scans" element={<Scans />} />
              <Route path="/scans/scandetails/:id" element={<ScanDetails />} />
              <Route path="/vulnerabilities" element={<Vulnerabilities />} />
              <Route
                path="/vulnerabilities/vulnerabilitydetails/:id"
                element={<VulnerabilityDetails />}
              />
              <Route path="/secrets" element={<Secrets />} />
              <Route path="/configurations" element={<Configurations />} />
              <Route path="/workflows" element={<Workflows />} />
              <Route
                path="/vulnerabilityclasses"
                element={<VulnerabilityClasses />}
              />
              <Route path="/tags" element={<Tags />} />
              <Route path="/twitter" element={<Twitter />} />
            </Routes>
          <div className="text-blue-gray-600">
            <Footer />
          </div>
        </div>
      </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
