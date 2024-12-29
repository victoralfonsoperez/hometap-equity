import { useState } from "react";
import "./index.css";
import { API_response, getAPIData } from "./utils/getAPIData";

function App() {
  const [apiData, setApiData] = useState<API_response>()
  const [loading, setLoading] = useState(false)
  async function search(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const inputValue = formData.get('address');
    const encodedValue = encodeURIComponent(inputValue as string)
    
    if (encodedValue) setLoading(true)
    const {response} = await getAPIData(encodedValue)
    
    if (response) {
      setApiData(response)
      setLoading(false)
    }
  }

console.log({apiData})

  return (
    <div className="container mx-auto md:container md:mx-auto">
      <h1 className="text-6xl">Hometap equity</h1>
      <form onSubmit={search}>
        <div className="space-y-12">
          <div className="border-b border-gray-900/10 pb-12">

            <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-4">
                <label
                  htmlFor="username"
                  className="block text-sm/6 text-lg/8 font-medium text-white-900"
                >
                  Equity search
                </label>
                <div className="mt-2">
                  <div className="flex items-center rounded-md bg-white pl-3 outline outline-1 -outline-offset-1 outline-gray-300 focus-within:outline focus-within:outline-2 focus-within:-outline-offset-2 focus-within:outline-indigo-600">
                    <div className="shrink-0 select-none text-base text-gray-500 sm:text-sm/6 pl-4 pr-4">
                      Address
                    </div>
                    <input
                      type="text"
                      name="address"
                      id="address"
                      className="block min-w-0 grow py-1.5 pl-1 pr-3 text-base text-white-900 placeholder:text-gray-500 focus:outline focus:outline-0 focus:bg-gray-700 focus:text-gray-200 sm:text-sm/6"
                      placeholder="Address"
                    />
                  </div>
                </div>
              </div>

              
            </div>
          </div>
        </div>

        <div className="mt-6 flex items-center justify-end gap-x-6">
          <button
            type="submit"
            className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Search
          </button>
        </div>
      </form>
      <div>
        {loading ? <p>Loading data...</p> : null}
        {apiData ? <h2 className="text-4xl mb-8">Results</h2>: null}
        <div className="flex flex-row">
          {apiData && apiData.source_1 ? <div className="w-1/2">
            <p><span>Bathrooms:</span> {apiData.source_1[0].bathrooms}</p>
            <p><span>Bedrooms:</span> {apiData.source_1[0].bedrooms}</p>
            <p><span>Year Built:</span> {apiData.source_1[0].yearBuilt}</p>
            <p><span>Property Type:</span> {apiData.source_1[0].propertyType}</p>
            <p><span>Sale Price:</span> {apiData.source_1[0].salePrice}</p>
            <p><span>Room Count:</span> {apiData.source_1[0].roomCount}</p>
          </div> : null}
          {apiData && apiData.source_2 ? <div className="w-1/2">
            <p><span>Bathrooms:</span> {apiData.source_2[0].bathrooms}</p>
            <p><span>Bedrooms:</span> {apiData.source_2[0].bedrooms}</p>
            <p><span>Year Built:</span> {apiData.source_2[0].yearBuilt}</p>
            <p><span>Property Type:</span> {apiData.source_2[0].propertyType}</p>
            <p><span>Sale Price:</span> {apiData.source_2[0].salePrice}</p>
            <p><span>Room Count:</span> {apiData.source_2[0].roomCount}</p>
          </div> : null}
        </div>
        
      </div>
    </div>
  );
}

export default App;
