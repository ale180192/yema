import { Injectable } from '@angular/core';
import { Appointment } from './appointment.model';
import { Subject } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { AuthService } from '../auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AppointmentService {
  private data: Appointment[] = [];
  private baseUrl =   environment.api_url;
  appointmentUpdated = new Subject<{ results: Appointment[], count: number }>();

  constructor(private client: HttpClient, private authService: AuthService) {}

  getAppointmentListener() {
    return this.appointmentUpdated.asObservable();
  }

  get(itemsPerPage: number, currentPage: number) {
    const queryParams = `?pagesize=${itemsPerPage}&page=${currentPage}`;
    let token = this.authService.getToken();
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': `Bearer ${token}`
      })
    };
    this.client.get<{ message: string; items: any; maxItems: number }>(
                `${this.baseUrl}/api/v1/appointments/list` + queryParams,
                httpOptions
              ).subscribe( (response: any) => {
                console.log('response is ', response);
                this.data = response.results;
                this.appointmentUpdated.next({
                  results: [...this.data],
                  count: response.count
                });
    });
  }

  getById(id: number){
    this.data.forEach( (appointmen: Appointment) => {
      // tslint:disable-next-line: curly
      if (appointmen.id === id )
        return appointmen;
      });
  }

  add(appointmen: Appointment) {
    // TODO: handler status codes of the response
    return this.client.post(`${this.baseUrl}/api/v1/appointments`, appointmen);
  }

  delete(id: number) {
    return this.client.delete(`${this.baseUrl}/api/v1/appointments/${id}`);
  }

}
