import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/layout/Header";
import Sidenav from "./components/layout/Sidenav";
import Footer from "./components/layout/Footer";

import Home from "./components/home/Home";
import Dashboard from "./components/home/Dashboard";

import Adaptors from "./components/apps/Adaptors";

import Scans from "./components/apps/Scans";
import ScanDetails from "./components/apps/scan/ScanDetails";

import Vulnerabilities from "./components/apps/Vulnerabilities";

import Secrets from "./components/apps/Secrets";

import Tags from "./components/configurations/Tags";
import Configurations from "./components/configurations/Configurations";
import Workflows from "./components/configurations/VulnerabilityClasses";
import VulnerabilityClasses from "./components/configurations/Workflows";

import Twitter from "./components/social/Twitter";
import VulnerabilityDetails from "./components/apps/vulnerability/VulnerabilityDetails";

function App() {
  return (
    <div className="App bg-gray-100">
      <div className="min-h-screen bg-blue-gray-50/50">
        <Sidenav />
        <div className="p-4 xl:ml-80">
          <Header />
          <BrowserRouter>
            <Routes>
              <Route path="/home" element={<Home />} />
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
          </BrowserRouter>
          <div className="text-blue-gray-600">
            <Footer />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
