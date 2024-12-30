# hometap-equity

hometap equity web app


## Requirements to run te application

In order to run the back and the frontend apps you need to install [Docker](https://www.docker.com/).

from the root folder you can run the following command to start both applications at the same time:

```bash
docker-compose up --build
```

and the following command to finish the process.

```bash
docker-compose down
```


### Architectural choices

#### Backend: FastAPI

FastAPI was selected for its combination of speed, simplicity, and modern features that are well-suited for rapid development. It’s one of the fastest web frameworks in Python, leveraging asynchronous programming out of the box to handle many requests concurrently. This makes it an excellent choice for applications that require fast response times or need to handle a high volume of requests.

FastAPI's automatic generation of OpenAPI and JSON Schema documentation significantly reduces setup time for API documentation and testing, it did allow me to quickly integrate API specifications into the development process. The framework’s strong reliance on Python type hints also enables better development tools, such as autocompletion and automatic error checking, which improves both productivity and code quality. With automatic request validation and minimal boilerplate, FastAPI did allow me to focus more on building features rather than managing infrastructure or writing repetitive code.

Additionally, FastAPI has built-in support for OAuth2, JWT authentication, and CORS, which makes it easy to implement common features like secure authentication and cross-origin resource sharing. This helped me avoid spending time on security-related configuration and allowed me to focus on delivering functional code quickly.

#### Frontend: Vite-React

On the frontend, I’ve opted for Vite paired with React. Vite is an extremely fast development tool that uses ESBuild under the hood to bundle code and optimize builds. This results in almost instant hot module reloading (HMR), allowing me to see frontend changes in real time without waiting for slow rebuilds. This speed is particularly important when working under tight deadlines as it reduces the feedback loop and accelerates development.

React's component-based architecture enabled me to build a maintainable, modular frontend that scales well. React’s popularity also means there is a wealth of resources, libraries, and community support available, reducing the time needed to solve common problems. Combined with Vite, React also benefits from fast production builds due to Vite's optimized bundling process, ensuring that the final application remains performant even as the project grows.

Vite’s native support for TypeScript, JSX, and CSS modules further streamlines the development process, offering built-in tooling and support for modern JavaScript features. Given that Vite is designed to work seamlessly with frameworks like React, that way I can spend less time configuring build tools and more time focusing on writing the application features.

#### Why This Stack?

Developer Productivity: Both FastAPI and Vite-React offer excellent developer experiences with fast feedback loops and minimal configuration overhead, allowing me to focus on building features rather than dealing with complex setups or slow build times.
Performance: FastAPI's asynchronous support and React's efficient rendering, paired with Vite's fast bundling, ensure that both the backend and frontend perform well under load.
Scalability: Both FastAPI and React are highly scalable, making it easy to extend the application as requirements evolve. The modular nature of React and the high-performance architecture of FastAPI allow for future growth without major rewrites.
Community and Support: Both FastAPI and Vite have strong, active communities. React’s widespread adoption ensures that finding solutions to common challenges will be straightforward, while FastAPI’s growing popularity and modern features ensure it’s future-proof for the backend.


### Next steps

While the application is functional, both the backend and frontend have significant room for improvement.

Backend
In the backend, the aggregated response logic can be optimized. Currently, there are areas where data consistency could be ensured better, particularly when interacting with third-party APIs. Properly typing the responses from these APIs would help catch errors earlier and ensure that data is consistently structured throughout the application. This would also improve maintainability and reduce the likelihood of runtime issues due to unexpected data formats.

Frontend
On the frontend, there is potential to extend and better test the types for the API responses. With more time, I would have implemented contract testing between the frontend and backend to ensure that both sides are aligned and avoid breaking changes. Additionally, implementing more comprehensive tests would help improve error handling across the application. Incorporating optimistic UI patterns would provide a smoother user experience by making the interface feel more responsive, especially during actions that involve backend communication.

Testing and Error Handling
Given more time, I would have also added unit and integration tests to both the frontend and backend. This would not only ensure better error handling but also make the codebase more robust and easier to maintain in the long term. Proper testing, combined with clear error handling strategies, would contribute to a more reliable and user-friendly application overall.
