import { Component, OnInit, AfterViewInit, ViewChild, OnDestroy } from '@angular/core';
import { CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA } from '@angular/core';
import { MatPaginator, MatSort, MatTableDataSource, MatDialog, MatDialogRef, MAT_DIALOG_DATA, PageEvent} from '@angular/material';
import { AppointmentService } from '../appointment.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Appointment } from '../appointment.model';
import { FabButton } from '../../shared/models/fab-button.model';
import { AppointmenDetailComponent } from '../appointment-detail/appointment-detail.component';

@Component({
  selector: 'app-api-schema-list',
  templateUrl: './appointment-list.component.html',
  styleUrls: ['./appointment-list.component.scss']
})
export class AppointmentListComponent implements OnInit, AfterViewInit, OnDestroy {

  dataSource: MatTableDataSource<Appointment>;
  displayedColumns: string[] = ['commentary', 'datetime', 'id'];
  data: Appointment[] = [];
  pageSizeOptions = [2, 5, 10, 20, 50];
  totalItems = 0;
  itemsPerPage = 5;
  currentPage = 1;
  isLoading = false;
  fabButtons: FabButton [] = [{icon: 'add', actionName: 'New appointment'}];
  private apiSchemaSubscription: Subscription;
  @ViewChild(MatPaginator, {read: true, static: false}) paginator: MatPaginator;
  @ViewChild(MatSort, {read: false, static: false}) sort: MatSort;

  constructor( private appointmentService: AppointmentService, private router: Router, private dialog: MatDialog ) {
    this.apiSchemaSubscription = appointmentService.getAppointmentListener().subscribe( response => {
      console.log('response updated', response);
      this.isLoading = false;
      this.totalItems = response.count;
      this.data = response.results;
      this.renderTable(this.data);
    } );

  }

  async ngOnInit() {
    this.appointmentService.get(this.itemsPerPage, this.currentPage);
    this.renderTable(this.data);
    console.log('paginator on init', this.paginator);
  }

  ngAfterViewInit(): void {
    console.log('afterviewinit');
    this.renderTable(this.data);

  }

  ngOnDestroy(): void {
    this.apiSchemaSubscription.unsubscribe();
  }

  renderTable(data) {
    this.dataSource = new MatTableDataSource(data);
    console.log('paginator on render table', this.paginator);

    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    this.isLoading = false;
  }

  refresh() {
    this.dataSource.data = this.data;
  }

  onChangedPage(pageData: PageEvent) {
    console.log('change pagedata', pageData);
    this.isLoading = true;
    this.currentPage = pageData.pageIndex + 1;
    this.itemsPerPage = pageData.pageSize;
    this.appointmentService.get(this.itemsPerPage, this.currentPage);
    this.renderTable(this.data);
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim();
    filterValue = filterValue.toLowerCase();
    this.dataSource.filter = filterValue;
  }

  edit(id: number) {
    console.log('click on edit for element', id);
    this.router.navigate(['apis/detail', id]);
  }

  add(apiSchema: Appointment) {
    console.log('add service');
    console.log(apiSchema);
    this.appointmentService.add(apiSchema).subscribe( response => {
      this.appointmentService.get(this.itemsPerPage, this.currentPage);
    } );
  }

  delete(id: number) {
    // TODO: FIX to delete the only element of the last page, the request fail because the querystring are wrong,
    // the server response us a 404 status code
    console.log('click on delete', id);
    this.appointmentService.delete(id).subscribe( response => {
      this.appointmentService.get(this.itemsPerPage, this.currentPage);
    });
  }

  fabButtonActionClick(action: FabButton) {
    console.log('action click', action);
    switch(action.icon) {
      case 'add': {
        this.openDialog();
      }
    }
  }

  openDialog() {
    const dialogRef = this.dialog.open(AppointmenDetailComponent, {
      width: '400px',
      data: []
    });
    dialogRef.afterClosed().subscribe(result => {
      console.log('call afterclose on list');
      console.log(result);
      switch ( result.event ) {
        case 'cancel': {
          console.log('on list element. cancel');
          break;
        }
        case 'create': {
          console.log('on list element. create');
          console.log(result.event, result.data);
          this.add(result.data);
          break;
        }
      }
    });
  }
}
