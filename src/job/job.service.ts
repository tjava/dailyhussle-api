import { Injectable } from '@nestjs/common';

@Injectable({})
export class JobService {
  test() {
    return { meg: 'hello from job' };
  }
}
