import * as React from 'react';
import {useState , useEffect} from 'react';
import './Body.css';
import MicIcon from '@mui/icons-material/Mic';
import Blink from 'react-blink-text';
import Dropdown from 'react-bootstrap/Dropdown';
import SplitButton from 'react-bootstrap/SplitButton';
import Button from 'react-bootstrap/Button';
import { ButtonGroup } from 'react-bootstrap';
import FrontPage from './FrontPage';


import { IconButton } from '@mui/material';
function Body() {
    const [msg, setMsg] = useState('Mic Off......');
    const [message, setMessage] = useState('');
    const [message2, setMessage2] = useState('');
    const [Language, setLan] = useState('en');
    const [Language2, setLan2] = useState('en');

    function handleClick() {
      setMsg("Speaking .......");
      // await fetch("/voice?lan="+Language).then((res) =>
      //     res.text().then((data) => {
      //       setMessage(data);
      //       setMsg("Mic Off ......");
      //     })
      // );
      
    };
    useEffect(() => {
      if(message!="")
      fetch("/api/?query="+message+"&lan="+Language+"&lan2="+Language2).then((res) =>
          res.text().then((data) => {
            console.log(typeof(data));
            console.log(data.search("<h1>Internal Server Error</h1>"));
            if(data.search("<h1>Internal Server Error</h1>")==-1)
              setMessage2(data);
            else
              setMessage2(" ");
              console.log(data);
          })
      );
      else
      setMessage2(" ");
  }, [message ,Language ,Language2]);
    const handleMessageChange = event => {
        setMessage(event.target.value);
        console.log(event.target.value);
        
    };

    const handleMessageChange2 = event => {
        setMessage2(event.target.value);
        console.log(event.target.value);
    };
  return (
    <div className="Body">
      <div className='input'>
        <div className='data'>
            <h2> Input Text </h2>
            <select id="Language" 
              onChange={(e) => setLan(e.target.value)}>
                    <option value="en">English</option>
                    <option value="hi">Hindi</option>
                    <option value="ja">Japanese</option>
                    <option value="zh-cn">Chinese</option>
                    <option value="fr">french</option>
                    <option value="it">Italian</option>
                    <option value="es">Spanish</option>      

            </select>
        </div>
        <textarea rows={15} cols={40} className='textArea'value={message}
        onChange={handleMessageChange}/>
        <div className='mic'>
          <IconButton size="small"  >
            <MicIcon></MicIcon>
          </IconButton>
          <Blink color='black' text={msg} fontSize='50'>
          {msg}
        </Blink> 
        </div>
      </div>
      
      <div className='answer'>
        <div className='data'>
            <h2> Translate </h2>
            <select id="Language" 
              onChange={(e) => setLan2(e.target.value)}>
                    <option value="en">English</option>
                    <option value="hi">Hindi</option>
                    <option value="ja">Japanese</option>
                    <option value="zh-cn">Chinese</option>
                    <option value="fr">french</option>
                    <option value="it">Italian</option>
                    <option value="es">Spanish</option>
            </select>
        </div>
        <textarea rows={15} cols={40} className='textArea' value={message2} />
      </div>
    </div>

  );
}

export default Body;
