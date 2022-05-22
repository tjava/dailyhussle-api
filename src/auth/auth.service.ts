import { Injectable } from '@nestjs/common';

@Injectable({})
export class AuthService {
  test() {
    return { meg: 'hello from auth' };
  }
}
