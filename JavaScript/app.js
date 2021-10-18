const Discord = require('discord.js.old');
const client = new Discord.Client({
    partials: ["MESSAGE"]
});
require('dotenv').config(); 

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 


var snipe = "";

client.on('messageDelete',msg => {
    snipe = msg.author.username + ": " + msg.content
    msg.channel.send(`Stop deleteing message ${msg.author.username}`)
});

client.on('message', msg => {
    const userMessage = msg.content;
    if(userMessage == "send nudes") {
       return msg.reply("fucche ta bacchai xas, gayera lito kha,")
    }

    if(userMessage === "$snipe" && snipe != "") {
        return msg.reply(snipe)
    }
    
  });


 
client.login(process.env.TOKEN);