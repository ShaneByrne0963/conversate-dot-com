const { TestEnvironment } = require('jest-environment-jsdom');
const convertPost = require('../posting');

describe('Posting', () => {
    describe('Post conversion to HTML', () => {
        test('Should return "<p>Hello</p>" for "Hello"', () => {
            expect(convertPost('Hello')).toBe('<p>Hello</p>');
        });
    });
});