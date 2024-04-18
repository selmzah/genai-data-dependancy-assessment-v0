import React, { useState } from 'react';
import AppExplorer from './components/app_explorer/AppExplorer';
import GraphExplorer from './components/graph_explorer/GraphExplorer';
import DatabaseHealthCheck from './components/neo4j_healthcheck/DatabaseHealthCheck';
import { Typography, Container, Box, Button, Drawer, List, ListItem, ListItemText, Divider} from "@mui/material";
import KeyboardReturnIcon from '@mui/icons-material/KeyboardReturn';
import './App.css';


function App() {
  const [selectedTab, setSelectedTab] = useState(0);
  const [isMenuOpen, setMenuOpen] = useState(false);

  const handleTabChange = (newValue) => {
    setSelectedTab(newValue);
    setMenuOpen(false); // Close the side menu when a tab is selected
  };

  return (
    <div className="App">
      {/* Title */}
      <Container sx={{ marginTop: '5px', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h6" sx={{ fontSize: '32px', fontFamily: 'CustomFont, Courier New, monospace', margin: 0 }}>
          Claudie
        </Typography>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
          <Typography sx={{ fontSize: '14px', fontFamily: 'Courier New, monospace' }}>
            by
          </Typography>
          <img
            src={require('./static/logo_cap_white.png')}
            alt="Claudie Logo"
            style={{ width: '100px', height: 'auto', marginLeft: '5px' }}
          />
        </div>
      </Container>

      {/* Side Menu (Vertical Toolbar) */}
        <Drawer
          anchor="left"
          open={isMenuOpen}
          onClose={() => setMenuOpen(false)}
          sx={{
            '& .MuiDrawer-paper': {
              width: '200px',
              padding: '16px',
            },
          }}
        >
          <List>
          <ListItem button onClick={() => handleTabChange(0)}>
              <ListItemText primary="Graph Explorer" />
            </ListItem>
            <Divider />
            <ListItem button onClick={() => handleTabChange(1)}>
              <ListItemText primary="Apps Explorer" />
            </ListItem>
            <Divider />
            <ListItem button onClick={() => handleTabChange(2)}>
              <ListItemText primary="Neo4j Healthcheck" />
            </ListItem>
            <Divider />
          </List>

          {/* Keyboard Return Icon */}
          <Box
            sx={{
              position: "absolute",
              bottom: "16px",
              right: "16px",
              cursor: "pointer",
              fontSize: "24px",
            }}
          >
            <KeyboardReturnIcon onClick={() => setMenuOpen(false)} />
          </Box>
        </Drawer>


      {/* Main Content */}
      <Container
        sx={{
          flex: 1, // Set 'flex' property to 1 to fill the available vertical space
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          marginLeft: '20px', // Add left margin to create space for the vertical toolbar
        }}
      >
        <Container sx={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
          <div style={{ display: selectedTab === 0 ? 'block' : 'none' }}>
            <GraphExplorer />
          </div>
          <div style={{ display: selectedTab === 1 ? 'block' : 'none' }}>
            <AppExplorer />
          </div>
          <div style={{ display: selectedTab === 2 ? 'block' : 'none' }}>
            <DatabaseHealthCheck />
          </div>
        </Container>
      </Container>


      {/* Button to Open Side Menu */}
      <Button
        variant="text"
        onClick={() => setMenuOpen(true)}
        sx={{
          position: 'fixed',
          top: '20px',
          left: '0',
          zIndex: '1000',
          fontSize: '18px',
          cursor: 'pointer',
          padding: '4px 12px',
          height: '24px',
        }}
      >
        ☰
      </Button>
    </div>
  );
}

export default App;
