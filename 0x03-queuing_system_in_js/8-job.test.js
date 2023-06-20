import { createQueue } from 'kue';
import { describe, it } from 'mocha';
import { expect } from 'chai';
import { spy } from 'sinon';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

const list = [
    {
        phoneNumber: '08067534875',
        message: 'This is the code 09876 to verify your account',
    },
    {
        phoneNumber: '09076454234',
        message: 'This is the code 14708 to verify your account',
    },
];

describe('createPushNotificationsJobs', () => {
    it('display a error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('hello', queue)).to.throw(Error, 'Jobs is not an array');
    });
    it('create two new jobs to the queue', () => {
        const queueSpy = spy(queue, 'create');
        createPushNotificationsJobs(list, queue);
        expect(queueSpy.calledTwice).to.be.true;
        queueSpy.restore();
    });
});
