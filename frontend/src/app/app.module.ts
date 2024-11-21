import { provideHttpClient } from '@angular/common/http'; // Provide HttpClient
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent, // Declare the root component
  ],
  imports: [
    BrowserModule, // Core Angular module for browser apps
  ],
  providers: [
    provideHttpClient(), // Provide HttpClient with the new configuration
  ],
  bootstrap: [AppComponent], // Bootstrap the main component
})
export class AppModule {}
