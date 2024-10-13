FROM node:22 AS build-stage
#RUN npm install -g http-server
#RUN npm install -g vue
WORKDIR /app
ENV VITE_BACKEND_URL='http://localhost/api/'

COPY package*.json ./
RUN npm install 
COPY . .
RUN npm run build

FROM nginx:1.27.2 AS production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
#COPY --from=build-stage /app/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]