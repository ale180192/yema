import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule, MatDialogModule } from '@angular/material';

import { AppointmentRoutingModule } from './appointment-routing.module';
import { AppointmentListComponent } from './appointment-list/appointment-list.component';
import { AppointmenDetailComponent } from './appointment-detail/appointment-detail.component';
import { SharedModule } from '../shared/shared.module';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
      AppointmentListComponent,
      AppointmenDetailComponent,
    ],
  imports: [
    CommonModule,
    AppointmentRoutingModule,
    MatTableModule,
    SharedModule,
    MatDialogModule,
  ],
  exports: []
})
export class AppointmentModule { }
