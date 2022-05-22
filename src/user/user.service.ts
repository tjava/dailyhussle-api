import { Injectable } from '@nestjs/common';

@Injectable({})
export class UserService {
  test() {
    return { meg: 'hello from user' };
  }
}
