import { Controller, Get } from '@nestjs/common';
import { JobService } from './job.service';

@Controller('api/job')
export class JobController {
  constructor(private jobService: JobService) {}

  @Get('test')
  test() {
    return this.jobService.test();
  }
}
