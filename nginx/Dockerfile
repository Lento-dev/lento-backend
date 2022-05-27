FROM node:12-alpine as build

WORKDIR /code

COPY ./lento-frontend/package.json .
RUN npm i
COPY ./lento-frontend .

RUN npm run build

FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY --from=build /code/build /usr/share/nginx/html
