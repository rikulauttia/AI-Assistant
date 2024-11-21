import { HttpClientModule } from '@angular/common/http'; // Required for HTTP requests
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // Required for [(ngModel)]
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent, // Declare AppComponent
  ],
  imports: [
    BrowserModule, // Required for Angular applications
    FormsModule, // Required for [(ngModel)]
    HttpClientModule, // Required for backend communication
  ],
  providers: [],
  bootstrap: [AppComponent], // Bootstraps AppComponent
})
export class AppModule {}
