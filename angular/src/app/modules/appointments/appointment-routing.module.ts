import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatButtonModule } from '@angular/material/button';

import { AppointmentListComponent } from './appointment-list/appointment-list.component';
import { AppointmenDetailComponent } from './appointment-detail/appointment-detail.component';
import { ReactiveFormsModule } from '@angular/forms';


const routes: Routes = [
  {
    path: 'list',
    component: AppointmentListComponent
  },
  {
    path: 'detail/:id',
    component: AppointmenDetailComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [
            RouterModule,
            MatFormFieldModule,
            ReactiveFormsModule,
            MatIconModule,
            MatInputModule,
            MatPaginatorModule,
            MatSortModule,
            MatButtonModule,
          ]
})
export class AppointmentRoutingModule { }
