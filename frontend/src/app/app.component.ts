import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
})
export class AppComponent {
  messages: { sender: string; text: string }[] = []; // Stores chat messages
  userMessage: string = ''; // Stores user input

  constructor(private http: HttpClient) {}

  sendMessage() {
    if (this.userMessage.trim() === '') {
      alert('Please enter a message.');
      return;
    }

    // Add user's message to the chat
    this.messages.push({ sender: 'You', text: this.userMessage });

    // Send the message to the backend
    this.http
      .post<{ response: string }>('http://127.0.0.1:5000/predict', {
        message: this.userMessage,
      })
      .subscribe(
        (response) => {
          // Add the bot's response to the chat
          this.messages.push({ sender: 'Bot', text: response.response });
        },
        (error) => {
          this.messages.push({
            sender: 'Bot',
            text: 'Error communicating with the server.',
          });
        }
      );

    // Clear the input field
    this.userMessage = '';
  }
}
