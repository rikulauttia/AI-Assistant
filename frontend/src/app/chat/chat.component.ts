import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-chat', // Correct selector with quotes
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})
export class ChatComponent {
  messages: { user: string; text: string }[] = [];
  userMessage: string = '';

  constructor(private http: HttpClient) {}

  sendMessage() {
    if (this.userMessage.trim()) {
      // Add user message to chat
      this.messages.push({ user: 'You', text: this.userMessage });

      // Send message to backend
      this.http
        .post<any>('http://127.0.0.1:5000/predict', {
          message: this.userMessage,
        })
        .subscribe(
          (response) => {
            this.messages.push({ user: 'Bot', text: response.response });
          },
          (error) => {
            this.messages.push({
              user: 'Bot',
              text: 'Error: Unable to fetch response.',
            });
          }
        );

      // Clear input field
      this.userMessage = '';
    }
  }
}
