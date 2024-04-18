import React, { useState } from 'react';
import { Paper, List, ListItem, ListItemText, TextField, Button, Box } from '@mui/material';
import SmartToyIcon from '@mui/icons-material/SmartToy';
import AccountBoxIcon from '@mui/icons-material/AccountBox';
import './GraphExplorer.css';

function GraphExplorer() {
  const apiBase = '/api';
  const [inputValue, setInputValue] = useState('');
  const [messages, setMessages] = useState([]);
  const [isFetching, setIsFetching] = useState(false);
  const [isButtonDisabled, setButtonDisabled] = useState(false);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSendMessage = () => {
    if (inputValue.trim() !== '') {
      setButtonDisabled(true)
      const userMessage = {
        user: true,
        content: inputValue,
      };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInputValue('');
      setIsFetching(true);

      // Call the API to get the robot's response
      fetch(`${apiBase}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: inputValue }),
      })
        .then((response) => response.json())
        .then((data) => {
          const answer = data.answer;

          const botMessage = {
            user: false,
            content: `${answer}`,
          };
          setIsFetching(false);
          setMessages((prevMessages) => [...prevMessages, botMessage]);
          setButtonDisabled(false);
        })
        .catch((error) => {
          console.error('Error:', error);
          setIsFetching(false);
          const errorMessage = {
            user: false,
            content: 'Sorry, I am having trouble understanding you right now.',
          };
          setMessages((prevMessages) => [...prevMessages, errorMessage]);
          setButtonDisabled(false);
        });
    }
  };

  const handleClearConversation = () => {
    fetch(`${apiBase}/clear_session`)
      .then((response) => response.text())
      .then(() => {
        setMessages([]);
      });
  };

  return (
    <div
      style={{
        position: 'fixed',
        bottom: 0,
        left: 0,
        right: 0,
        height: 'calc(100% - 100px)',
        maxWidth: '50%',
        margin: 'auto',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'flex-end',
        boxSizing: 'border-box',
      }}
    >
      <Paper
        elevation={0}
        sx={{
          flex: 1,
          overflowY: 'auto',
          overflowX: 'hidden',
          padding: '0rem',
          display: 'flex',
          flexDirection: 'column-reverse',
          width: '100%',
        }}
      >
        <List>
          {messages.map((message, index) => (
            <ListItem key={index}>
              <ListItemText
                sx={{
                  fontFamily: 'Courier New, monospace',
                  textAlign: message.user ? 'right' : 'left',
                }}
                primary={
                  message.user ? (
                    <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end' }}>
                       Me
                      <AccountBoxIcon style={{ marginLeft: '0.5rem' }} />
                    </span>
                  ) : (
                    <span style={{ display: 'flex', alignItems: 'center' }}>
                      <SmartToyIcon style={{ marginRight: '0.5rem' }} />
                      Claudie
                    </span>
                  )
                }
                primaryTypographyProps={{ variant: 'body1' }}
                secondaryTypographyProps={{ variant: 'body2', component: 'div'}}
                secondary={<div>
                    {message.content}
                    {/* Utiliser dangerouslySetInnerHTML pour insérer le lien formaté */}
                    {message.source && (
                      <div dangerouslySetInnerHTML={{ __html: message.source }} />
                    )}
                </div>}
                disableTypography
              />
            </ListItem>
          ))}
          {isFetching && (
            <ListItem>
              <ListItemText
                sx={{
                  fontFamily: 'Courier New, monospace',
                  display: 'flex',
                  alignItems: 'center',
                }}
                primaryTypographyProps={{
                  variant: 'body1',
                  display: 'flex',
                  alignItems: 'center',
                }}
                secondaryTypographyProps={{ variant: 'body2' }}
                disableTypography
                primary={
                  <span style={{ display: 'flex', alignItems: 'center' }}>
                    <SmartToyIcon style={{ marginRight: '0.5rem' }} />
                    Claudie
                  </span>
                }
                secondary={
                  <Box className="chat-message typing-message">
                    <Box className="message-content" sx={{ marginLeft: '0.5em' }}>
                      <span className="typing-text">is typing </span>
                      <span className="jumping-dots">
                        <span className="dot-1">.</span>
                        <span className="dot-2">.</span>
                        <span className="dot-3">.</span>
                      </span>
                    </Box>
                  </Box>
                }
              />
            </ListItem>
          )}
        </List>
      </Paper>
      <TextField
        label="Message"
        disabled = {isButtonDisabled}
        fullWidth
        value={inputValue}
        onChange={handleInputChange}
        variant="outlined"
        style={{ marginTop: '1rem' }}
        onKeyDown={(event) => {
          if (event.key === 'Enter') {
            handleSendMessage();
          }
        }}
      />
      <Box sx={{ marginTop: '1rem' }}>
        <Button variant="contained" color="primary" onClick={handleSendMessage} disabled = {isButtonDisabled}>
          Ask Claudie
        </Button>
        <Button variant="outlined" color="primary" onClick={handleClearConversation} sx={{ marginLeft: '1rem' }} disabled = {isButtonDisabled}>
          Clear conversation
        </Button>
      </Box>
      {/* Add a margin of 1rem to separate the buttons from the bottom of the page */}
      <Box sx={{ marginBottom: '1rem' }} />
    </div>
  );
}

export default GraphExplorer;
