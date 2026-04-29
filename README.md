\section{QuickChat AI - RAG Based Chatbot}

\subsection{Overview}
QuickChat AI is a Streamlit-based chatbot that combines:

\begin{itemize}
\item \textbf{PDF Question Answering} using RAG (Retrieval Augmented Generation)
\item \textbf{Live Google Search} for latest information
\item \textbf{Conversation Memory}
\item \textbf{LLM Powered Responses} using Groq Llama Model
\end{itemize}

\subsection{Tech Stack}

\begin{itemize}
\item Python
\item Streamlit
\item LangChain
\item LangGraph
\item Groq API
\item ChromaDB
\item HuggingFace Embeddings
\end{itemize}

\subsection{Features}

\begin{enumerate}
\item Upload PDF files
\item Ask questions from uploaded PDF
\item Search real-time information from Google
\item Chat history memory
\item Fast responses using Groq LLM
\end{enumerate}

\subsection{Main Libraries Used}

\begin{verbatim}
streamlit
langchain
langgraph
langchain_groq
langchain_chroma
langchain_huggingface
python-dotenv
\end{verbatim}

\subsection{Workflow}

\begin{enumerate}
\item User uploads PDF
\item PDF converted into chunks
\item Embeddings generated using MiniLM model
\item Stored in Chroma Vector DB
\item Retriever fetches relevant chunks
\item LLM answers using context
\item For current topics, Google Search tool is used
\end{enumerate}

\subsection{LLM Configuration}

\begin{verbatim}
Model = llama-3.3-70b-versatile
Temperature = 0.3
\end{verbatim}

\subsection{RAG Pipeline}

\begin{verbatim}
PDF -> Text Splitter -> Embeddings -> Chroma DB -> Retriever -> LLM
\end{verbatim}

\subsection{Agent Tools}

\begin{itemize}
\item rag\_tool : Search uploaded PDF
\item google\_search : Search latest/current info
\end{itemize}

\subsection{Run Project}

\begin{verbatim}
streamlit run app.py
\end{verbatim}

\subsection{Environment Variables}

\begin{verbatim}
GROQ_API_KEY=your_key
SERPER_API_KEY=your_key
\end{verbatim}

\subsection{Author}

Disha Panjla